export const serverListConfig = {
	rowData: [],
	columnDefs: [
		{headerName: 'Server Name', field: 'server_name', class:'col-sm-5'},
		{headerName: 'Comment', field: 'comment', class:'col-sm-5'}
	],
	rowMenu: [
	  {headerName: 'Edit', path: '/edit', field: 'server_id' , pathTemplate: '/server/{{server_id}}/edit'},
	  {headerName: 'Delete', path: '/delete', field: 'server_id'},
	  {headerName: 'Add/Remove SanGroup', path: '/present', field: 'server_id', pathTemplate: '/server/{{server_id}}/san-group/link/'}
	 ],
 message:"No Server Defined",	 
 isSubGrouping: true,
  subGroupOptions: [
    {
      rowData: [],
      parentField: 'sangroup',
      columnDefs: [
        {headerName: 'San Group', field: 'sangroup_name'}
      ]
    }
  ]
};