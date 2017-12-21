/**
 * created by Venkatesh
 * @type
 */
export const poolsListOptions = {
  rowData: [],
  columnDefs: [
    {headerName: 'Position', field: 'position'},
    {headerName: 'Status', field: 'status'},
    {headerName: 'Serial No', field: 'serialnumber'},
    {headerName: 'FirmWare Version', field: 'fwversion'},
    {headerName: 'Capacity', field: 'capacity'},
    {headerName: 'Identify', field: 'toggle'},
  ],
  rowMenu: [],
  isSubGrouping: false,
  subGroupOptions: [],
  applyStyle:[{columnName:'status',module:'pool' }]
};
