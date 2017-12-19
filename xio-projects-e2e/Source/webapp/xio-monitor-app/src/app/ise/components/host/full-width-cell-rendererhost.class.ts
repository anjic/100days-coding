export class FullWidthCellRenderer {
  public eGui: any;

  public init(params) {
    // create the cell
    let eTemp = document.createElement('div');
    eTemp.innerHTML = this.getTemplate(params);
    // this.eGui = eTemp.firstElementChild;
    this.eGui = eTemp;

  };

  // gets called once when grid ready to insert the element
  public getGui() {
    return this.eGui;
  };

  public getTemplate(params) {

    let allocations: any = '';
    if (params.data.allocations.hasOwnProperty('allocations')) {
      allocations = params.data.allocations.allocations;
    } else {
      allocations = [params.data.allocations.allocation];
    }

    var template = '<div class="row nested-dt-header" style="background: rgba(158, 158, 158, 0.18);padding-left: 4%;">'
      + '<div class="col-sm-4">VOLUME NAME</div>'

      + '<div class="col-sm-4">LUN</div>'
      + '<div class="col-sm-4">GUID</div>'
      + '</div>';
    template += '<div class="nested-dt" style="overflow:auto;height:150px" >';

    if (allocations.length) {
      let volume_arr = [];
      for (let i = 0; i < allocations.length; i++) {

        if (volume_arr.indexOf(allocations[i].volumename) < 0) {
          volume_arr.push(allocations[i].volumename)
          template += '<div class="row " style="padding-left: 4%;" >'
            + '<div class="col-sm-4 ">' + allocations[i].volumename + '</div>'
            + '<div class="col-sm-4">' + allocations[i].lun + '</div>'
            + '<div class="col-sm-4">' + allocations[i].globalid.slice(0, 31) + '</div>'
            + '</div>';
        }
      }
    } else {
      template += '<div class="row " style="padding-left: 4%;padding-top:15px;" >'
        + '<div class="col-sm-12 text-warnning">Volumes yet to be allocated</div>'
        + '</div>';
    }
    template = template + '</div>'
    return template;

  };
}
