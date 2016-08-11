'use strict';

angular.module('biblioApp.state2', ['ui.router'])

    .config(['$stateProvider', function ($stateProvider) {
        $stateProvider.state('/state2', {
            url: '/state2',
            templateUrl: 'partial/components/view2/state.html'
        });
    }]);