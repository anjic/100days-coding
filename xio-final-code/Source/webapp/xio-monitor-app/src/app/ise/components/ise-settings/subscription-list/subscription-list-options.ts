export const listConfig = {
  rowData: [],
  columnDefs: [
    {headerName: 'ID', field: 'id', class: 'col-md-2'},
    {headerName: 'Subscription Status', field: 'setting', class: 'col-md-2'},
    {headerName: 'Type', field: 'type', class: 'col-md-1'},
    {headerName: 'SSL', field: 'ssl', class: 'col-md-1'},
    {headerName: 'Proxy', field: 'proxy', class: 'col-md-1'},
    {headerName: 'Proxy Address', field: 'proxy_address', class: 'col-md-1'},
    {headerName: 'Proxy Username', field: 'proxy_username', class: 'col-md-1'},
    {headerName: 'Proxy Password', field: 'proxy_password', class: 'col-md-1'}
  ],
  rowMenu: [
    {headerName: 'Edit', path: '/edit', field: 'id', pathTemplate: '/ise/{{ise_id}}/settings/edit/{{id}}/{{type}}'},
    {headerName: 'Delete', path: '/delete', field: 'id'},
    
  ],
  isSubGrouping: false  

 
};