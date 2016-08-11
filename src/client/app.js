'use strict';

angular
    .module('biblioApp', [
            'ui.router',
            'biblioApp.state1',
            'biblioApp.state2'
    ])
    // .config(['$routeProvider', function ($routeProvider) {
    //     $routeProvider.otherwise({redirectTo: '/'});
    // }])
    .config(function ($stateProvider, $urlRouterProvider, $locationProvider) {
        $urlRouterProvider.otherwise("/state1");
        
        
        // $locationProvider.html5Mode(true);

        // $templateCache.put('templateId.html', 'This is the content of the template');
        
        // $stateProvider
        //     .state('state1', {
        //         url: '/state1',
        //         template: '<h1>Hello, main</h1>',
        //         controller: 'biblioAppCtrl'
        //     })
        //     .state('state2', {
        //         url: "/state2",
        //         templateUrl: "partial/components/view2/state.html"
        //     })
    })
    .run(['$rootScope', function ($rootScope) {
        console.log('!!!')
    }]);