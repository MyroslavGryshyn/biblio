'use strict';

angular.module('biblioApp.state1', ['ui.router'])

    .config(['$stateProvider', function ($stateProvider) {
        $stateProvider.state('/state1', {
            url: '/state1',
            templateUrl: 'partial/components/view1/state.html'
        });
    }]);