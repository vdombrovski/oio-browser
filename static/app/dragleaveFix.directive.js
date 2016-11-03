var app = angular.module("oioBrowser");

app.directive('fixdragleave',goFixDragLeave);

function goFixDragLeave() {
    return {
        restrict: 'EA',
        link: function(scope, element, attrs) {
          var element=angular.element(element);
          element.on('dragleave', function () {
              element.removeClass("nv-file-over");
          });
        }
    }
};
