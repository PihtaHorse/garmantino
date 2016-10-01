"use strict"

n = paths.length;

window.onload = function() {
	setTimeout(function() {
		for(i=0; i<n; i++){
		    new Image().src = paths[i];
        }

	}, 100);
};