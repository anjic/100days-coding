
export interface Pools {
	status: {
		_attr: {
			string: string;
			value: number;
		},
		details: {
			_attr: {
				value: string;
			},
			detail: string;
		}
	},
	available: {
		_attr: {
			total: string;
		},
		byredundancy: {
			"raid-1": number;
			"raid-0": number;
			"raid-5": number;
		}
	},
	used: {
		_attr: {
			total: string;
		},
		byredundancy: {
			"raid-1": number;
			"raid-0": number;
			"raid-5": number;
		}
	},
	name: string;
	globalid: string;
	provisioned: {
		_attr: {
			total: string;
		},
		byredundancy: {
			"raid-1": number;
			"raid-0": number;
			"raid-5": number;
		}
	},
	SlowSheettotal: number;
	media: {
		medium: {
			tier: {
				tier: string;
				_attr: {
					string: string;
					value: number;
				}
			},
			_attr: {
				self: string;
			},
			health: number;
		},
		_attr: {
			self: string;
		}
	},
	_attr: {
		self: string;
	},
	Flashavailable: {
		_attr: {
			total: string;
		},
		byredundancy: {
			"raid-1": number;
			"raid-0": number;
			"raid-5": number;
		}
	},
	FastSheettotal: number;
	Flashcapacity: number;
	FastSheetallocated: number;
	Flashused: {
		_attr: {
			total: string;
		},
		byredundancy: {
			"raid-1": number;
			"raid-0": number;
			"raid-5": number;
		}
	},
	volumes: {
		_attr: {
			self: string;
		},
		volumes: [
			{
				_attr: {
					self: string;
				},
				globalid: string;
			}

		]
	},
	ThinThreshold: number;
	SlowSheetallocated: number;
	Flashprovisioned: {
		_attr: {
			total: string;
		},
		byredundancy: {
			"raid-1": number;
			"raid-0": number;
			"raid-5": number;
		}
	},
	id: number;
	Flashquota: number;
	size: number;
}




