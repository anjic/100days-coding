/**
 * Created by Dominic on 9/05/2017.
 */
export interface RowMenu {
  headerName: string;
  field: string;
  path: string;
  pathTemplate?: string;
}

export interface ColumnDef  {
  headerName: string;
  field: string;
  value?: string | number;
}

export interface GridOptions {
  rowHeight?: number;
  columnDefs: Array<ColumnDef>;
  rowData: Array<Object>;
  rowMenu?: Array<RowMenu>;
  deleteCb?: Function;
  isSubGrouping?: boolean;
  subGroupOptions?: Array<GridOptions>;
  subGroupData?: Array<Object>;
  parentField?: string;
}
