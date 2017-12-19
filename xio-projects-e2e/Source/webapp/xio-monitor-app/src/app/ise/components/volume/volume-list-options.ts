export const volumeListConfig = {
  rowData: [],
  columnDefs: [
    {headerName: 'NAME', field: 'volume_name', class:"col-sm-3 alloc-width"},
    {headerName: 'SIZE', field: 'size', class:"col-sm-1 size-width"},
    {headerName: 'RAID', field: 'raid', class:"col-sm-1 raid-width"},
    {headerName: 'POOL', field: 'pool', class:"col-sm-1 pool-width"},
    {headerName: 'PROVISIONING', field: 'provisioning', class:"col-sm-2 provision-width"},
    {headerName: 'TYPE', field: 'dedupe_type', class:'col-sm-1'},
    {headerName: 'ALLOC', field: 'allocation', class:'col-sm-1'},
    {headerName: 'STATUS', field: 'status', class:'col-sm-3 status-width'},

  ],
  rowMenu: [
    {headerName: 'Edit', path: '/edit', field: 'id' , pathTemplate: '/ise/{{ise_id}}/volume/edit/{{guiid}}'},
    {headerName: 'Delete', path: '/delete', field: 'id'}
  ],
  isSubGrouping: true,
  subGroupOptions: [
    {
      rowData: [],
      parentField: '',
      columnDefs: [
        {headerName: 'QOS', field: 'qos', class:'col-sm-1'},
        {headerName: 'IOPS MIN', field: 'iopsmin', class:'col-sm-1'},
        {headerName: 'IOPS MAX', field: 'iopsmax',class:'col-sm-1'},
        {headerName: 'IOPS Burst', field: 'iopsburst',class:'col-sm-1'},
        {headerName: 'CREATED DATE', field: 'create_date', class:'col-sm-2'},
        {headerName: 'GUID', field: 'guiid', class:'col-sm'},
      ]
    },
    {
      rowData: [],
      parentField: '',
      columnDefs: [
        {headerName: 'COMMENT', field: 'comment', class:'col-sm'}
      ]
    },
    {
      rowData: [],
      parentField: 'allocations',
      columnDefs: [
        {headerName: 'WWN Group Name', field: 'hostname', class:'col-sm'},
        {headerName: 'LUN', field: 'lun',class:'col-sm'}
      ]
    }
  ]
};