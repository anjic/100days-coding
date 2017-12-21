/**
 * Created by Dominic on 07-09-2017.
 */
export const listConfig = {
  rowData: [],
  columnDefs: [
    {headerName: 'Name', field: 'name', class:'col-sm-5'},
    {headerName: 'Comment', field: 'comment', class:'col-sm-5'}
  ],
  rowMenu: [
    {headerName: 'Edit', path: '/edit', field: 'id' , pathTemplate: '/ise/{{ise_id}}/host/edit/{{id}}'},
    {headerName: 'Delete', path: '/delete', field: 'id'},
    {headerName: 'Present / Un-Present', path: '/present', field: 'id', pathTemplate: '/ise/{{ise_id}}/host/{{id}}/present'}
  ],
  isSubGrouping: true,
  subGroupOptions: [
    {
      rowData: [],
      parentField: 'allocation',
      columnDefs: [
        {headerName: 'Volume Name', field: 'volumename', width: 100, rowGroupIndex: 0},
        {headerName: 'LUN', field: 'lun', width: 100, rowGroupIndex: 0},
        {headerName: 'GUID', field: 'globalid', width: 100, rowGroupIndex: 0}
      ]
    }
  ]
};
