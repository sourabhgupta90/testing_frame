var restifyModule = angular.module('restify', ['ui.bootstrap', 'ngRoute', 'ngCookies', 'ngTable']).config(['$routeProvider',

function($routeProvider) {
    $routeProvider.when('/', {
        controller : 'testingAuthRulesControllers',
        templateUrl : '/services',
    });
}]);

restifyModule.controller('serviceController', function($scope) {
    console.log("serviceController");
});