/**
 * Created by Dominic on 7/20/2017.
 */
declare let d3;
export const chartConfig = {
  chart: {
    type: 'lineChart',
    height: 250,
    margin: {
      top: 20,
      right: 20,
      bottom: 40,
      left: 55
    },
    x: function (d) {
      return new Date(d['x']);
    },
    y: function (d) {
      return d.y;
    },
    useInteractiveGuideline: true,
    xAxis: {
      axisLabel: 'Time',
      tickFormat: function (d) {
        return d3.time.format.utc('%H:%M')(new Date(d))
      }
    }
  }
}