/**
 * Created by Venkatesh on 9/21/2017.
 */
export const sangroupListOptions = {
  rowData: [],
  columnDefs: [
    { headerName: 'ISE Name', field: 'ise_name', class:'col-sm-3' },
    { headerName: 'Host Name', field: 'name', class:'col-sm-3' },
    { headerName: 'Comment', field: 'host_comment', class:'col-sm-5' }
  ],
  rowMenu: [
    { headerName: 'Edit', path: '/edit', field: 'id' , pathTemplate: '/ise/{{ise_id}}/host/edit/{{host_id}}/' },
    { headerName: 'Delete', path: '/delete', field: 'id' }
  ],
  isSubGrouping: false,
  subGroupOptions: []
};
