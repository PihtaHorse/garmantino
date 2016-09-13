var wrapper = document.getElementsByClassName('hexagons-wrapper')[0];
var rowsNumber = wrapper.children.length;
var footer = document.getElementById('footer');
var oddRow = "'hexagon-row-odd'", evenRow = "'hexagon-row-even'";

if(rowsNumber % 2){
    footer.insertAdjacentHTML('beforebegin', newRow(5, oddRow));
}
else {
    footer.insertAdjacentHTML('beforebegin', newRow(6, evenRow));
    footer.insertAdjacentHTML('beforebegin', newRow(5, oddRow));
}

if(rowsNumber == 1) {
    footer.insertAdjacentHTML('beforebegin', newRow(6, evenRow));
    footer.insertAdjacentHTML('beforebegin', newRow(5, oddRow));
}
