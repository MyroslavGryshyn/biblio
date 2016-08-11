(function (){
    'use strict';

    angular
        .module('biblioApp', [
                'ui.router'
        ])
        .config(function ($stateProvider, $urlRouterProvider) {
            $urlRouterProvider.otherwise("/404");

            $stateProvider
                .state('mainState', {
                    url: '/main-state',
                    template: '<h1>Hello, main</h1>',
                    controller: 'biblioAppCtrl'
            })
        })
        .run(['$rootScope', function ($rootScope) {
            $rootScope.itHasBeenClicked = true;
        }]);
});
