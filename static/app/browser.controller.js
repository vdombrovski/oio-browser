var app = angular.module("oioBrowser");

app.controller("browserController", ['$scope', 'apiRequest', 'FileUploader', getController]);


function getController($scope, apiRequest, FileUploader) {
  $scope.objects = [];
  $scope.containers = [];
  $scope.containerInfo = {};
  $scope.currentCont = "";
  $scope.searchedObject = {"s": ""};
  $scope.ccontainer = {"c": ""};
  $scope.uploader = new FileUploader({"autoUpload": true});
  $scope.didSearch = false;
  $scope.created = false;

  $scope.apiRequest = new apiRequest();

  $scope.download = getDownloadUrl;
  $scope.preview = getPreviewUrl;
  $scope.changeCurrentContainer = changeContainer;
  $scope.doSearch = doSearch;
  $scope.createContainer = createContainer;

  (function() {
    $scope.apiRequest.getContainers(function(res) {
      $scope.containers = res.data.containers;
      $scope.currentCont = res.data.containers[0][0];
      $scope.containerInfo = res.data.info;
      getObjects($scope.currentCont);
      $scope.uploader.url = '/api/containers/' + $scope.currentCont + '/objects';

      $scope.uploader.onSuccessItem = function(d) {
        getObjects($scope.currentCont);
      }
    });
  })()

  function getObjects(container) {
    $scope.apiRequest.getObjects(container, function(res) {
      $scope.objects = res.data.objects;
    });
  }

  function createContainer(ccontainer) {
    $scope.apiRequest.createContainer(ccontainer, function(res) {
      $scope.created = true;
      $scope.currentCont = ccontainer;
      $scope.uploader.url = '/api/containers/' + $scope.currentCont + '/objects';
      getObjects($scope.currentCont);
      $scope.apiRequest.getContainers(function(res) {
        $scope.containers = res.data.containers;
        $scope.containerInfo = res.data.info;
      });
    });
  }

  function doSearch(searchedObject) {
    $scope.apiRequest.searchObjects($scope.currentCont, searchedObject, function(res) {
      $scope.objects = res.data.objects;
      $scope.didSearch = true;
    });
  }

  function getDownloadUrl(name) {
    return "/api/containers/" + $scope.currentCont + "/objects/" + name + "/download";
  }

  function getPreviewUrl(name) {
    return "/api/containers/" + $scope.currentCont + "/objects/" + name + "/preview";
  }

  function changeContainer(name) {
    $scope.currentCont = name;
    $scope.uploader.url = '/api/containers/' + name + '/objects';
    getObjects(name);
  }
}
