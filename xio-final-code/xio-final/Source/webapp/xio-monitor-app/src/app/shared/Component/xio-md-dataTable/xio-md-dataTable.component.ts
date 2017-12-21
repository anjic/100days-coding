import {Component, OnInit, OnDestroy, OnChanges, Input, Output, EventEmitter, DoCheck} from '@angular/core';
import {ColumnDef, GridOptions} from '../../../common/Metadata/xio.dataTable';


@Component({
  selector: 'xio-md-dataTable',
  templateUrl: './xio-md-dataTable.component.html',
  styleUrls: ['./xio-md-dataTable.component.scss']
})
export class XioMdDataTableComponent implements OnInit, OnDestroy, OnChanges, DoCheck {

  @Input() gridOptions;
  @Input() isSubGroup: boolean;
  @Input() subGroupData: Array<object> = [];
  @Output()
  toggleBtnClick: EventEmitter<any> = new EventEmitter<any>();


  public _options: GridOptions = null;

  constructor() {
    this.isSubGroup = false;
  }

  ngOnInit() {
  }
  
   
  /**
   * Method for getting nested data in table
   * @namespace xio.XioMdDataTableComponent
   * @param {any} fields
   * @param {any} data
   * @method getNestedData
   */

  getNestedData(fields, data) {
    if (fields && fields.indexOf('.') > 1) {
      let _nest = fields.split('.'),
        _data = null;
      _nest.forEach((k) => {
        if (_data == null && data.hasOwnProperty(k)) {
          _data = data[k];
         } else if (_data.hasOwnProperty(k)) {
          _data = _data[k];
         }
      });
      return (Array.isArray(_data) ? _data : [_data]);
    }else if ( fields ) {
      return (Array.isArray(data[fields]) ? data[fields] : [data[fields]]);
    } else {
      return (Array.isArray(data) ? data : [data]);
    }
  }

   /**
   * Method for parsing data in table
   * @namespace xio.XioMdDataTableComponent
   * @param {any} options
   * @param {any} data
   * @method parseData
   */

  parseData(data, options) {
    if (options.columnDefs && data) {
      let _rowData = [];
      options.columnDefs.forEach((c) => {
        c.value = data[c.field];
        _rowData.push(c);
      });
      return _rowData;
    }else {
      return [];
    }
  }


   /**
   * Method for sorting data in table
   * @namespace xio.XioMdDataTableComponent
   * @param {any} event
   * @method onSortByChange
   */

  onSortByChange(e) {
    this.gridOptions.rowData = this.gridOptions.rowData.sort((a, b): number => {
      if (a[e.value] > b[e.value]) {
        return 1;
       } else if (a[e.value] < b[e.value]) {
        return -1;
       } else {
        return 0;
       }  
    });
  }


   /**
   * Method for filtering data in table
   * @namespace xio.XioMdDataTableComponent
   * @param {any} event
   * @method onFilterByChange
   */


  onFilterByChange(e) {
    let _searchText = e.currentTarget.value;
    if (!this._options) {
      this._options = Object.assign({}, this.gridOptions);
    if (!this.isSubGroup) {
      if (_searchText.length !== 0) {
        this.gridOptions.rowData = this._options.rowData.filter((d) => {
          let _dstr = JSON.stringify(d);
          if (_dstr.indexOf(_searchText) > 0) {
            return d;
          }
        });
      }  else {
        this.gridOptions.rowData = this._options.rowData;
      }
    }
   }
  }

  ngOnChanges() {
  }

  ngOnDestroy() {
  }

  ngDoCheck() {
  }
  
   /**
   * Method for passing argument to the identify in pools
   * @namespace xio.XioMdDataTableComponent
   * @param {any} arg
   * @method masterToggleLed
   */


  masterToggleLed( arg) {
    arg['ledEnabled'] = arg.currentTarget ? true : false;
    this.toggleBtnClick.emit(arg);
    
  }

}
