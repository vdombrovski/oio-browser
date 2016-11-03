var app = angular.module("oioBrowser");

app.factory("apiRequest", ['$http', getFactory]);

function getFactory($http) {
  var service = {
    'getObjects': getObjects,
    'getContainers': getContainers,
    'searchObjects': searchObjects
  }
  return function() {
    return service;
  };

  function getObjects(container, cb) {
      $http.get('/api/containers/' + container +'/objects').then(cb);
  }

  function searchObjects(container, searched, cb) {
      $http.get('/api/containers/' + container +'/objects/search/' + searched).then(cb);
  }

  function getContainers(cb) {
      $http.get('/api/containers').then(cb);
  }

}
