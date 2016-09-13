var newRow = function(hexagonsNumber, rowClass){
    var hexagon = "<div class='hexagon'><div class='hexagon-part1'><div class='hexagon-part2'> </div></div></div>";
    var row = "<div class=" + rowClass + ">";
    for (i = 0; i < hexagonsNumber; i++) {
        row += hexagon
    }
    row += "</div>";

    return row;
};