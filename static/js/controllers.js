'use strict';

function CodeCtrl($scope, $http, $location, $timeout) {
  $(document).keydown(function(event) {
    var e = window.event || event;
    if (e.keyCode == 13 && e.shiftKey) {  // shift-enter
      $scope.runCode($scope.code);
    } else if (e.keyCode == 33) {  // page up
      $scope.location.path("/" + $scope.prevChapter());
      $scope.$apply();
      return false;
    } else if (e.keyCode == 34) {  // page down
      $scope.location.path("/" + $scope.nextChapter());
      $scope.$apply();
      return false;
    }
  });

  $scope.location = $location;

  // This naively assumes that the dirty state is "sticky" unless you force a
  // full recomputation. Works for most purposes in the UI.
  $scope._dirty = false;
  $scope.dirty = function(force_recompute) {
    if (force_recompute || !$scope._dirty) {
      $scope._dirty = ($scope.tutorial != undefined &&
                       $scope.code != $scope.tutorial.code);
    }
    return $scope._dirty;
  };

  $scope.storageKey = function() {
    return "pytut-" + $scope.tutorial.name;
  };

  $scope.saveCode = function() {
    if ($scope.tutorial === undefined) {
      return;
    }
    var dirty = $scope.dirty(true);

    // Save to the internal JS cache first.
    $scope.tutorial.userCode = (dirty) ? $scope.code : undefined;

    // Also save to HTML5 local storage if possible.
    // This protects users against refresh and browser crashes.
    if (typeof(Storage) != "undefined") {
      if ($scope.tutorial.userCode === undefined) {
        localStorage.removeItem($scope.storageKey());
      } else {
        localStorage[$scope.storageKey()] = JSON.stringify({
          time_ms: +new Date(),
          user_code: $scope.tutorial.userCode,
        });
      }
    }
  };

  $scope.loadCode = function() {
    if ($scope.tutorial === undefined) {
      return;
    }

    // Get from localStorage if possible.
    if (typeof(Storage) != "undefined") {
      var val = localStorage[$scope.storageKey()];
      if (val !== undefined) {
        // TODO: Age out old things?
        $scope.tutorial.userCode = JSON.parse(val).user_code;
      }
    }
    // If there is data in userCode now, then we display that. Otherwise we get
    // the tutorial code and display that.
    if ($scope.tutorial.userCode !== undefined) {
      $scope.code = $scope.tutorial.userCode;
    } else {
      $scope.code = $scope.tutorial.code;
    }
    $scope.dirty(true);  // Force dirty bit recomputation.
  };
  // TOC should be off when we start.
  $scope.tocShowing = false;

  $scope.parseTutorial = function(text) {
    var lines = text.split(/\r\n|\n|\r/);
    // If the file starts with comments right at the beginning, strip them off
    // (typically directives to editors).
    var cur = 0;
    for (; cur<lines.length; cur++) {
      if (lines[cur].trim() && lines[cur].search(/^\s*#.*$/) < 0) {
        break;
      }
    }
    // Remaining text is treated as a whole.
    text = lines.slice(cur).join('\n');
    var groups = text.match(/\s*"""([^]*?)\n\s*([^]*?)"""\s+([^]*)$/m)
    if (!groups) {
      return {title: "", description: "", code: ""};
    }

    return {
      title: groups[1].replace(/\\(["'])/g, '$1'),
      description: groups[2].replace(/\\(["'])/g, '$1'),
      code: groups[3].replace(/^(\s*)__doc__\s*=\s*/, '$1'),
    };
  };

  var tutorialsPending = -1;

  function loadTutorial(index, path) {
    $http.get(path).
      success(function(text) {
        var parsed = $scope.parseTutorial(text);
        $scope.tutorials[index] = {
          name: name,
          index: index,
          title: parsed.title,
          description: parsed.description,
          code: parsed.code,
        };
        tutorialsPending--;
      });
  }

  $http.get("tutorials/tutorials.json").
    success(function(tutNames) {
      $scope.tutorials = new Array(tutNames.length);
      tutorialsPending = tutNames.length;

      for (var i=0; i<tutNames.length; i++) {
        loadTutorial(i, "tutorials/" + tutNames[i] + ".py");
      }

      // Triggered (below) when no more tutorials are pending.
      var onTutorialsLoaded = function() {
        $scope.tutorial = $scope.tutorials[$scope.chapter-1];
        $scope.loadCode();

        // Redirect to the first page if none is specified.
        if (!$location.path()) {
          $location.path('/1').replace();
        }

        // Notice when the path changes and use that to
        // navigate, but only after we actually have
        // data.
        $scope.$watch('location.path()', function(path) {
          var newChapter = +path.replace(/^[/]/, '');
          if (newChapter == 0) {
            // Special value - don't go to chapter 0.
            newChapter = $scope.chapter;
            $scope.location.path("/" + $scope.chapter).replace();
          }
          $scope.tocShowing = false;
          if (newChapter != $scope.chapter) {
            $scope.saveCode();
            $scope.chapter = newChapter;
            $scope.tutorial = $scope.tutorials[newChapter-1];
            $scope.loadCode();
            $scope.clearOutput();
            $(document.body).scrollTop(0);
          }
        });
      };

      // Finally, we wait until tutorialsPending is zero.
      var checkPending = function() {
        if (tutorialsPending > 0) {
          window.setTimeout(checkPending, 1);
        } else {
          onTutorialsLoaded();
        }
      };
      window.setTimeout(checkPending, 1);
    });

  // Set up a handy timer that watches when _time changes and starts a new
  // timeout to change it. It's a bit more elegant than creating a function
  // and creating a timeout from a timeout.
  $scope._time = new Date();
  $scope.$watch('_time', function() {
    $scope.saveCode();  // Also forces dirty bit recomputation.
    $timeout(function(){
      $scope._time = new Date();
    }, 5000);
  });

  $scope.addOutputText = function(text) {
    $scope._addText(text, "stdout");
  };

  $scope.addErrorText = function(text) {
    $scope._addText(text, "stderr");
  };

  $scope._addText = function(text, elementClass) {
    var output = document.getElementById("output");
    var scrolled = output.scrollHeight - output.clientHeight - output.scrollTop;
    var scrollDown = scrolled < 12;
    var pre = document.createElement("pre");
    pre.className = elementClass;
    pre.appendChild(document.createTextNode(text));
    output.appendChild(pre);
    if (scrollDown) {
      output.scrollTop = output.scrollHeight - output.clientHeight;
    }
  };

  // Creates a function that accepts code and runs it on the server.
  function makeRunOnServer() {
    return function(code) {
      $scope.clearOutput();
      $http.post("/runcode", code).success(function(data) {
        $scope.addOutputText(data.stdout);
        $scope.addErrorText(data.stderr);
      });
    };
  }

  // Creates a function that runs code on PyPy.js.
  // onLoaded is called when the vm has finished initializing.
  function makeRunOnPyPyJS(onLoaded) {
    // Initialize PyPy.js
    var vm = new PyPyJS({
      stdout: $scope.addOutputText,
      stderr: $scope.addErrorText,
      autoLoadModules: false,
    });
    vm.ready.then(onLoaded);
    return function(code) {
      if (!$scope.vmLoaded) {
        console.log("vm not ready - ignoring request to run code")
        return;
      }
      $scope.clearOutput();
      try {
        vm.loadModuleData("contextlib").then(function() {
          // Clean up the global namespace, get the help function, and create a doctest.
          vm.execfile("../../../../../_preamble.py").then(function() {
            return vm.exec(code).catch(function(err) {
              console.log(err);
              $scope.addErrorText(err.trace);
            });
          });
        });
      } catch (err) {
        console.log(err);
        $scope.addErrorText("Internal Error: " + $scope.prettyError(err));
      }
    };
  }

  // prettyError is used to make javascript exceptions easier on the eyes.
  $scope.prettyError = function(err) {
    // If we are dealing with Firefox, just output the message.
    if (err.stack[0] == '@') {
      return err.name + ": " + err.message;
    }
    var lines = err.stack.split(/\r\n|\r|\n/);
    var output = [lines[0]];
    // Now only keep lines that have <anonymous> as the file name, and filter
    // out irrelevant text from those.
    for (var i = 1; i < lines.length; i++) {
      var line = lines[i];
      if (line.match(/^\s*at .*runCode/)) {
        break;
      }
      line = line.replace(/\([^()]*\)/, '');
      line = line.replace(/\s*\(.*:(\d+):(\d+)\)$/, ":$1:$2");
      line = line.replace("Object.eval", "_Main_");
      output.push(line);
    }
    return output.join("\n");
  };

  // If PyPyJS loaded, we can use that. Otherwise, run this thing on the server.
  (function(document, window, undefined) {
    $scope.vmLoaded = false;

    if (window.PyPyJS !== undefined) {
      console.log("using client-side PyPy.js implementation");
      $scope.runCode = makeRunOnPyPyJS(function() {
        console.log("vm loaded");
        $scope.vmLoaded = true;
      });
    } else {
      console.log("using server-side Python implementation");
      $scope.runCode = makeRunOnServer();
      $scope.vmLoaded = true;
    }
  }(document, window))

  // This is useful for binding keys in the code window to do
  // nothing at all. We can't, for whatever reason, define this
  // function in-line.
  //
  // Note that we use this for Shift-Enter because it is a
  // document-wide keystroke that should run the code, but if
  // you're in the code window it causes a newline to be
  // inserted, too.
  $scope.doNothing = function(e) {}

  $scope.clearOutput = function() {
    var output = document.getElementById("output");
    while (output.lastChild) {
      output.removeChild(output.lastChild);
    }
  }

  $scope.clearCode = function() {
    $scope.code = "";
  }

  $scope.revertCode = function() {
    $scope.code = $scope.tutorial.code;
    // Force dirty bit recomputation:
    $scope.dirty(true);
  };

  $scope.revertAll = function() {
    // Remove all local storage if we have it.
    if (typeof(Storage) != "undefined") {
      localStorage.clear();
    }
    $scope.revertCode();
  };

  $scope.prevChapter = function() {
    if ($scope.tutorial == undefined || $scope.tutorial.index <= 0) {
      return 0;  // special value meaning don't go there.
    }
    return $scope.tutorial.index;  // chapter - 1
  }

  $scope.nextChapter = function() {
    if ($scope.tutorial == undefined ||
        $scope.tutorial.index >= $scope.tutorials.length - 1) {
      return 0;  // special value - don't go there.
    }
    return $scope.tutorial.index + 2;  // chapter + 1
  }
}
