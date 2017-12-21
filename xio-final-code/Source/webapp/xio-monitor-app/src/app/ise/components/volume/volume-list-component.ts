/**
 * Created by Dominic on 07-09-2017.
 * THIS FILE IS NOT USED -- SEE volume-list-options.ts
 */
export const listConfig = {
  rowData: [],
  columnDefs: [
    {headerName: 'VOLUME NAME', field: 'name', width: 200,sort: 'asc', rowGroupIndex: 0},
    {headerName: 'SIZE', field: 'size', width: 80, minWidth: 50, maxWidth: 100},
    {
      headerName: 'RAID',
      field: 'configurationpolicy.redundancy._attr.string',
      width: 100,
      minWidth: 40,
      maxWidth: 100
    },
    {
      headerName: 'POOL',
      field: 'pools.pool',
      width: 100,
      cellRenderer: this.poolCellRenderer,
      pool: this.pools_list
    },
    {headerName: 'CREATED DATE', field: 'createdate', width: 150, minWidth: 50, maxWidth: 1000},
    {headerName: 'ALLOCATION (%)', field: 'allocpercent', width: 150, minWidth: 50, maxWidth: 100},
    {headerName: 'PROVISIONING', field: 'alloctype._attr.string', width: 150, minWidth: 50, maxWidth: 500},
    {headerName: 'DEDUPE TYPE', field: 'type', width: 150, minWidth: 50, maxWidth: 500},
    {
      headerName: 'STATUS',
      field: 'status._attr.string',
      width: 150,
      minWidth: 50,
      maxWidth: 500,
      cellRenderer: this.getstatus
    }

  ],
  rowMenu: [
    {headerName: 'Edit', path: '/edit', field: 'id' , pathTemplate: '/ise/{{ise_id}}/host/edit/{{id}}'},
    {headerName: 'Delete', path: '/delete', field: 'id'}
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
