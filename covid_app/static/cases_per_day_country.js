function renderChart(charData, title) {
    var chart = new CanvasJS.Chart("chartContainer", {
        animationEnabled: true,
        title:{
            text: title
        },
        axisX:{
            valueFormatString: "DD MMM"
        },
        axisY: {
            title: "Number of Cases",
            scaleBreaks: {
                autoCalculate: true
            }
        },
        data: [{
            type: "line",
            xValueFormatString: "DD MMM",
            color: "#F08080",
            dataPoints: charData
        }]
    });
    chart.render();

}