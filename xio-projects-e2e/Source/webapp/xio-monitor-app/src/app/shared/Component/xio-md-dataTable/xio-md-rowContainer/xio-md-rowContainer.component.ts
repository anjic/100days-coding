import {Component, OnInit, Input, OnChanges, ChangeDetectionStrategy, Output, EventEmitter} from '@angular/core';
import {ColumnDef, GridOptions, RowMenu} from '../../../../common/Metadata/xio.dataTable';


@Component({
  selector: 'xio-md-rowContainer',
  templateUrl: './xio-md-rowContainer.component.html',
  styleUrls: ['./xio-md-rowContainer.component.scss']
})
export class XioMdRowContainerComponent implements OnInit, OnChanges {

  @Input() data: object;
  @Input() gridOptions;
  @Input() isSubGroup: boolean;
  @Input() rowObject: Object;
  @Input() headerRow: boolean;
  public value: string;

  @Output()
  toggleUpdated: EventEmitter<any>  = new EventEmitter<any>();

  public isCollapse: boolean;

  constructor() {
    this.isCollapse = true;
    this.isSubGroup = false;
    this.headerRow = false;
  }

  ngOnInit() {
  }
  
  /**
   * Method for toggling the rotate-icon
   * @namespace xio.XioMdRowContainerComponent
   * @param {any} event
   * @method toggle
   */

  toggle(e) {
    this.isCollapse = !this.isCollapse;
    e.target.classList.toggle('rotate-icon');
  }
  
   /**
   * Method for resolving the path
   * @namespace xio.XioMdRowContainerComponent
   * @param {any} template
   * @method resolvePath
   */

  resolvePath(template, data) {
    if (template && template.indexOf('{{id}}')) {
      template = template.replace('{{id}}', data['id']);
    }
    if (template && template.indexOf('{{ise_id}}')) {
      template = template.replace('{{ise_id}}', data['ise_id']);
    }
    if (template && template.indexOf('{{sangroup_id}}')) {
      template = template.replace('{{sangroup_id}}', data['sangroup_id']);
    }
    if (template && template.indexOf('{{guiid}}')) {
      template = template.replace('{{guiid}}', data['guiid']);
    }
    if (template && template.indexOf('{{host_id}}')) {
      template = template.replace('{{host_id}}', data['host_id']);
    }
    if (template && template.indexOf('{{server_id}}')) {
      template = template.replace('{{server_id}}', data['server_id']);
    }
    if (template && template.indexOf('{{type}}')) {
      template = template.replace('{{type}}', data['type']);
    }
    return template || '';
  }

  ngOnChanges() {

  }

    /**
   * Method for toggling the identify in Pools
   * @namespace xio.XioMdRowContainerComponent
   * @param {any} event
   * @method toggleLed
   */

  toggleLed(event, _value) {
    _value['rowObject'] = this.rowObject;
    _value['led'] = event.checked ? 'enabled' : 'disabled';
    this.value = _value;
    this.toggleUpdated.emit(this.value);
  }

   /**
   * Method for applying styles
   * @namespace xio.XioMdRowContainerComponent
   * @param {any} cellInfo
   * @method applyStyle
   */


  applyStyle(cellInfo) {
    if ( this.gridOptions.hasOwnProperty('applyStyle') ) {
       if ( this.gridOptions['applyStyle'][0]['module'] === 'pool' &&
          this.gridOptions['applyStyle'][0]['columnName'] === 'status') {
          if ( cellInfo.value === 'Drive Failed' ||
              cellInfo.value === 'Disruptive' ||
              cellInfo.value === 'Unknown' ||
              cellInfo.value ===  'Not Installed') {
              return 'pool_red';
          }
        }else if (this.gridOptions['applyStyle'][0]['module'] === 'user' &&
                this.gridOptions['applyStyle'][0]['columnName'] === 'is_active') {
           if ( cellInfo.value === 'Yes' ) {
             return 'pools_available_capacity';
           } else if ( cellInfo.value === 'No' ) {
             return 'text-danger';
           }
         }
    }
  }

}
