export const listConfig = {
  rowData: [],
  columnDefs: [
    {headerName: 'User Name', field: 'name', class: 'col-md'},
    {headerName: 'User Email', field: 'email', class: 'col-md'},
   
  ],
  rowMenu: [
    {headerName: 'Edit', path: '/edit', field: 'id',pathTemplate:'/ise/{{ise_id}}/email/edit/{{id}}'},
    {headerName: 'Delete', path:'/delete', field: 'id'},
   
  ],
  isSubGrouping: false,
  subGroupOptions: []
};