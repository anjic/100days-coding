export const sanGroupListConfig = {
  rowData: [],
  columnDefs: [
    { headerName: 'Name', field: 'sangroup_name', class: 'col-sm-5' },
    { headerName: 'Comment', field: 'comment', class: 'col-sm-5' }
  ],
  rowMenu: [
    { headerName: 'Edit', path: '/edit', field: 'id', pathTemplate: '/san-group/edit/{{sangroup_id}}' },
    { headerName: 'Delete', path: '/delete', field: 'id' }
  ],
  message: "No Sangroup Defined",
  isSubGrouping: false
};
