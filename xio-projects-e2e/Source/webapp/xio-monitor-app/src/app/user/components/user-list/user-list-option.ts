export const listConfig = {
  rowData: [],
  columnDefs: [
    { headerName: 'USER NAME', field: 'username', class: 'col-md' },
    { headerName: 'FIRST NAME', field: 'first_name', class: 'col-md' },
    { headerName: 'Last Name', field: 'last_name', class: 'col-md' },
    { headerName: 'Email', field: 'email', class: 'col-md' }
  ],
  rowMenu: [
    { headerName: 'Edit', path: '/edit', field: 'id', pathTemplate: '/user/edit/{{id}}' },
    { headerName: 'Delete', path: '/delete', field: 'id' },

  ],
  isSubGrouping: false,
};