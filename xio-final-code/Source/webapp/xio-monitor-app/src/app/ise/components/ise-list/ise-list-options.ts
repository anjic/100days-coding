/**
 * Created by Dominic on 7/27/2017.
 */

export const listConfig = {
  rowData: [],
  columnDefs: [
    { headerName: 'Name', field: 'ise_name', class: 'col-md' },
    { headerName: 'Serial Number', field: 'serial_no', class: 'col-md' },
    { headerName: 'MRC 1 ', field: 'ip_primary', class: 'col-md' },
    { headerName: 'MRC 2 ', field: 'ip_secondary', class: 'col-md' }
  ],
  rowMenu: [
    { headerName: 'Edit', path: '/edit', field: 'id', pathTemplate: '/ise/{{id}}/edit' },
    { headerName: 'Delete', path: '/delete', field: 'id' },
    { headerName: 'Change Password', path: '/changePwd', field: 'id', pathTemplate: '/ise/{{id}}/change-pwd' },
    { headerName: 'Add/Remove ISE', path: '/present', field: 'id', pathTemplate: '/ise/{{id}}/san-group/link/' },
    { headerName: 'Update New IP', path: '/ip-update', field: 'id', pathTemplate: '/ise/{{id}}/ip-update' }
  ],
  isSubGrouping: true,
  message: "No ISE Defined",
  subGroupOptions: [
    {
      rowData: [],
      parentField: 'sangroup',
      columnDefs: [
        { headerName: 'San Group', field: 'sangroup_name' }
      ]
    }
  ]
};

