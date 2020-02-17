angular.module('runcodeFilters', []).
  filter('inplaceif', function() {
    return function(cond, tval, fval) {
      return cond ? tval : fval;
    };
  }).
  filter('paragraphs', function() {
    var inline_format = function(paragraph) {
      if (paragraph.match(/^\s/)) {
        return paragraph;
      }
      // Basic formatting.
      // Note the use of [\s\S] to get around the fact that javascript does
      // not have a "dotall" flag.
      paragraph = paragraph.replace(
        /(^|\W)(\||_|\*{1,2})(\S|\S[\s\S]*?\S)\2(?=\W|$)/mg,
        function(_, leader, delimiter, content) {
          tag = {
            '_': function(x) {return "<em>" + x + "</em>";},
            '*': function(x) {return "<strong>" + x + "</strong>";},
            '**': function(x) {return "<em><strong>" + x + "</strong></em>";},
            '|': function(x) {return '<span class=code>' + x + '</span>';},
          }[delimiter];
          return leader + tag(content);
        });
      return paragraph;
    }
    return function(input) {
      if (input !== undefined && input != "") {
        // Normalize newlines.
        input = input.replace(
          /\r\n|\n\r|\r|&#13;&#10;|&#10;&#13;|&#13;|&#10;/g, '\n');
        // Get paragraphs.
        var ps = input.split("\n\n");
        // Replace list item paragraphs with appropriate markup.
        var in_list = false;
        for (i in ps) {
          var paragraph = ps[i];
          if (ps[i].slice(0, 2) == "- ") {
            var prefix = "<li>";
            var suffix = "</li>";
            if (!in_list) {
              in_list = true;
              prefix = "<ul>" + prefix;
            }
            ps[i] =
              prefix +
              inline_format(paragraph.slice(2, paragraph.length)) +
              suffix;
          } else {
            var prefix = "<p>";
            var suffix = "</p>";
            if (paragraph.match(/^[\w\s]+$/)) {
              prefix = "<h2>"
              suffix = "</h2>"
            }
            if (paragraph.match(/^\s+/)) {
              prefix = "<pre>\n"
              suffix = "\n</pre>"
            }
            if (in_list) {
              in_list = false;
              prefix = "</ul>\n" + prefix;
            }
            ps[i] = prefix + inline_format(paragraph) + suffix;
          }
        }
        // Rejoin with paragraph tags.
        return ps.join("");
      }
      return "";
    };
  });
