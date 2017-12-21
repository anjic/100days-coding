export interface SANGroup {
	comment: string;
	created_by: string;
	created_date: string;
	is_delete: boolean;
	ise: {id: number, ise_name: string}[];
	modified_by: string;
	sangroup_id: number;
	sangroup_name: string;
	updated_date: string;
}

export interface SanGroupISE {
	id: number;
	ip_primary: string;
	ip_secondary: string;
	ise_name: string;
	raw_data: string;
	serial_no: string;
	time_stamp: string;
}

export interface GetSanIseData {
	endpoints: number;
	hosts: number;
	id: number;
	ip_primary: string;
	ip_secondary: string;
	ise_name: string;
	pools: number;
	raw_data: string;
	serial_no: string;
	size: {available: number, total_size: number, total_used: number};
	status: string;
	time_stamp: string;
	volumes: number;
}