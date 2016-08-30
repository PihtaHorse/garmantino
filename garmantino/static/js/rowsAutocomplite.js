function onElementHeightChange(elm, callback){
    var lastHeight = elm.clientHeight, newHeight;
    (function run(){
        newHeight = elm.clientHeight;
        if( lastHeight != newHeight )
            callback();
        lastHeight = newHeight;

        if( elm.onElementHeightChangeTimer )
            clearTimeout(elm.onElementHeightChangeTimer);

        elm.onElementHeightChangeTimer = setTimeout(run, 200);
    })();
}

function getDocHeight() {
    var D = document;
    return Math.max(
        D.body.scrollHeight, D.documentElement.scrollHeight,
        D.body.offsetHeight, D.documentElement.offsetHeight,
        D.body.clientHeight, D.documentElement.clientHeight
    );
}


onElementHeightChange(document.body, function(){
    D = document;
    console.log('scrollHeight: ' + D.body.scrollHeight.toString());
    console.log('offsetHeight: ' + D.body.offsetHeight.toString());
    console.log('clientHeight: ' + D.body.clientHeight.toString());
    console.log('scrollHeight: ' + D.documentElement.scrollHeight.toString());
    console.log('offsetHeight: ' + D.documentElement.offsetHeight.toString());
    console.log('clientHeight: ' + D.documentElement.clientHeight.toString());
    console.log('height: ' + getDocHeight().toString());
});

document.body.addEventListener("resize", function(){
    D = document;
    console.log('scrollHeight: ' + D.body.scrollHeight.toString());
    console.log('offsetHeight: ' + D.body.offsetHeight.toString());
    console.log('clientHeight: ' + D.body.clientHeight.toString());
    console.log('scrollHeight: ' + D.documentElement.scrollHeight.toString());
    console.log('offsetHeight: ' + D.documentElement.offsetHeight.toString());
    console.log('clientHeight: ' + D.documentElement.clientHeight.toString());
    console.log('height: ' + getDocHeight().toString());
});

