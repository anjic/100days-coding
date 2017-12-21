export class FullWidthCellRenderer {
  public eGui: any;
  // gets called once before the renderer is used
  public init(params) {
    // create the cell
    let eTemp = document.createElement('div');
    eTemp.innerHTML = this.getTemplate(params);
    this.eGui = eTemp;
  };

  public getGui() {
    return this.eGui;
  };

  public getTemplate(params) {
    // the flower row shares the same data as the parent row
    let data = params.node.data;
    var template = '<div class="row nested-dt-header" style="background: rgba(158, 158, 158, 0.18);padding-left: 4%;">'
      + '<div class="col-sm-3">QOS</div>'
      + '<div class="col-sm-3">IOPS MIN</div>'
      + '<div class="col-sm-3">IOPS MAX</div>'
      + '<div class="col-sm-3">IOPS BURST</div>'
      + '</div>';

    template += '<div class="row " style="padding-left: 4%;" >'
      + '<div class="col-sm-3 ">' + data.qosmode._attr.string + '</div>'
      + '<div class="col-sm-3 ">' + (data.IOPSmin == 0 ? 'notset': data.IOPSmin)+'</div>'
      + '<div class="col-sm-3 ">' + (data.IOPSmax == 0 ? 'notset': data.IOPSmax) + '</div>'
      + '<div class="col-sm-3 ">' + (data.IOPSburst == 0 ? 'notset': data.IOPSburst)+ '</div>'
      + '</div>'
      + '<span>&nbsp; &nbsp;  &nbsp;</span>';

    template += '<div class="row nested-dt-header" style="background: rgba(158, 158, 158, 0.18);padding-left: 4%;">'
      + '<div class="col-sm-3">Host</div>'
      + '<div class="col-sm-3">LUN</div>'
      + '<div class="col-sm-3">GUID</div>'
      + '</div>';
     
    if(data.lun.length != 0) {
      console.log("****");
      for (let i = 0; i < data.lun.length; i++) {
        template += '<div class="row " style="padding-left: 4%;" >'
          + '<div class="col-sm-3 ">' + data.hostname[i] + '</div>'
          + '<div class="col-sm-3">' + data.lun[i] + '</div>'
          + '<div class="col-sm-3">' + data.globalid + '</div>'
          + '</div>';
      }
    }
    else{    
      template += '<div class="row " style="padding-left: 4%;" >'
          + '<div class="col-sm-3 ">' + data.hostname + '</div>'
          + '<div class="col-sm-3">' + data.lun + '</div>'
          + '<div class="col-sm-3">' + data.globalid+ '</div>'
          + '</div>';
      
    }
  
    template = '<div class=\'nested-dt\'>' + template + '</div>'
    return template;
  };
}
