/**
 * Created by Dominic on 7/10/2017.
 */
import {createSelector} from 'reselect';
import {ActionReducer} from '@ngrx/store';


/**
 * The compose function is one of our most handy tools. In basic terms, you give
 * it any number of functions and it returns a function. This new function
 * takes a value and chains it through every composed function, returning
 * the output.
 *
 * More: https://drboolean.gitbooks.io/mostly-adequate-guide/content/ch5.html
 */
import {compose} from '@ngrx/core/compose';

/**
 * storeFreeze prevents state from being mutated. When mutation occurs, an
 * exception will be thrown. This is useful during development mode to
 * ensure that none of the reducers accidentally mutates the state.
 */
import {storeFreeze} from 'ngrx-store-freeze';

/**
 * combineReducers is another useful metareducer that takes a map of reducer
 * functions and creates a new reducer that gathers the values
 * of each reducer and stores them using the reducer's key. Think of it
 * almost like a database, where every reducer is a table in the db.
 *
 * More: https://egghead.io/lessons/javascript-redux-implementing-combinereducers-from-scratch
 */
import {combineReducers} from '@ngrx/store';


/**
 * Every reducer module's default export is the reducer function itself. In
 * addition, each module should export a type or interface that describes
 * the state of the reducer plus any selector functions. The `* as`
 * notation packages up all of the exports into a single object.
 */
import * as email from './email.reducer';
import * as user from './user.reducer';
import * as sg from './sangroup.reducer';
import * as hw from './hardware.reducer';
import * as settings from './ise-settings.reducers';
import * as hosts from './hosts.reducer';
import * as iseManage from './ise-management.reducers';
import * as volume from './volume.reducer';
import * as pools from './pools.reducer';
import * as menu from './menu.reducers';
import * as server from './server.reducer';

/**
 * As mentioned, we treat each reducer like a table in a database. This means
 * our top level state interface is just a map of keys to inner state types.
 */

export interface State {
  email: email.State;
  user: user.State;
  sanGroup: sg.State;
  hardware: hw.State;
  iseSettings: settings.State;
  hosts:hosts.State;
  iseManage: iseManage.State;
  volume:volume.State;
  pools:pools.State;
  menu: menu.State;
  server:server.State;
}


/**
 * Because metareducers take a reducer function and return a new reducer,
 * we can use our compose helper to chain them together. Here we are
 * using combineReducers to make our top level reducer, and then
 * wrapping that in storeLogger. Remember that compose applies
 * the result from right to left.
 */
const reducers = {
  email: email.reducer,
  user: user.reducer,
  sanGroup: sg.reducer,
  hardware:hw.reducer,
  iseSettings: settings.reducer,
  hosts:hosts.reducer,
  iseManage: iseManage.reducer,
  volume:volume.reducer,
  pools:pools.reducer,
  menu: menu.reducer,
  server:server.reducer,
};


//const developmentReducer: ActionReducer<State> = compose(storeFreeze, combineReducers)(reducers);
//Removed since freezing manipulation of object at run time
//For ref :
const developmentReducer: ActionReducer<State> = compose(combineReducers)(reducers);
// const productionReducer: ActionReducer<State> = combineReducers(reducers);

export function reducer(state: State, action: any) {
  // TODO to be done after setting Env Variable
  // if (environment.production) {
  //   return productionReducer(state, action);
  // } else {
  //   return developmentReducer(state, action);
  // }
  return developmentReducer(state, action);
}

/**
 * A selector function is a map function factory. We pass it parameters and it
 * returns a function that maps from the larger state tree into a smaller
 * piece of state. This selector simply selects the `books` state.
 */
// export const getEmailLst = (state: State) => state.email || [];

export const getEmailState = (state: State) => state.email;
export const getSanGroupState = (state: State) => state.sanGroup;
export const getUserState = (state: State) => state.user;
export const getHardwareState = (state: State) => state.hardware;
export const getISESettingsState = (state: State) => state.iseSettings;
export const getHostsState = (state: State) => state.hosts;
export const getISEManagementState = (state: State) => state.iseManage;
export const getVolumesState = (state: State) => state.volume;
export const getPoolsState = (state: State) => state.pools;
export const getMenuState = (state: State) => state.menu;
export const getServerState = (state:State) => state.server;

/**
 * Every reducer module exports selector functions, however child reducers
 * have no knowledge of the overall state tree. To make them useable, we
 * need to make new selectors that wrap them.
 *
 * The createSelector function from the reselect library creates
 * very efficient selectors that are memoized and only recompute when arguments change.
 * The created selectors can also be composed together to select different
 * pieces of state.
 */
// User Management
export const getUserLstState = createSelector(getUserState, user.getUserLst);
export const getUserInfo = createSelector(getUserState, user.getUser);
export const getControllerListState = createSelector(getHardwareState, hw.getControllerList);
export const getLoginedUser = createSelector(getUserState, user.getAuthInfo);
export const getUserIdState = createSelector(getUserState, user.getUser);

// export const getEmailLsit = createSelector(getISEState, email.getAllEmail );

export const getEmailLst = createSelector(getEmailState, email.getEmailLst);
export const getSanGroupLst = createSelector(getSanGroupState, sg.getSanGroupLst);
export const getSanGroupISEMap = createSelector(getSanGroupState, sg.getSanGroupISELstMap);
export const getSanGroupHostLst = createSelector(getSanGroupState, sg.getSanGroupHostLst);
export const getSanGroupInfoLst = createSelector(getSanGroupState, sg.getSanGroupISELstInfo);

//Server
export const getServerLstState = createSelector(getServerState, server.getServerLst);
export const getServerInfo = createSelector(getServerState, server.getServer);
export const getServerWwn = createSelector(getServerState, server.getWwn)
export const getServerWwnGroups = createSelector(getServerState, server.getAllWwnGroups)
export const getServerAllWwnGroups = createSelector(getServerState, server.getAllServerWwnGroups)
export const getServerSideWwnGroups = createSelector(getServerState, server.getServerSideWwnGroups)


//Hardware
export const getControllerList = createSelector(getHardwareState, hw.getControllerList);
export const geNetworkState = createSelector(getHardwareState, hw.getNetworkList);
export const gePowerSupplyState = createSelector(getHardwareState, hw.getPowerSupplyList);
export const geDataPAcState = createSelector(getHardwareState, hw.getDataPacList);
export const getFansState = createSelector(getHardwareState, hw.getFansList);

// Advance Settings
export const getSNMPTraps = createSelector(getISESettingsState, settings.getTraps);
export const getChronoTimeZone = createSelector(getISESettingsState, settings.getChronometer);
export const getSNMPList = createSelector(getISESettingsState, settings.getSnmpLst);
export const getISESubcription = createSelector(getISESettingsState, settings.getSubcriptionLst);
export const getLedStatus = createSelector(getISESettingsState, settings.getLedStatus);
export const getButtonStatus = createSelector(getISESettingsState,settings.getIsebuttonstatus);


//Volumes
export const getAllVolumesState = createSelector(getVolumesState, volume.getAllVolumesList);
export const getVolumeState = createSelector(getVolumesState, volume.getVolume);
export const totalSize = createSelector(getVolumesState, volume.totalSize);

//Pools
export const getAllPoolsState = createSelector(getPoolsState, pools.getAllPoolsList);
export const getDrivesListState = createSelector(getPoolsState, pools.getDrivesList);
export const getDrivesPerfomanceListState = createSelector(getPoolsState, pools.getDrivesPerformaceList);
export const getMediumListState = createSelector(getPoolsState, pools.getMediumList);
export const getRatioState = createSelector(getPoolsState, pools.getRatio);

//Hosts
export const getAllHostsList = createSelector(getHostsState, hosts.getAllHosts);
export const getHost = createSelector(getHostsState, hosts.getHost);


//ISE Management
export const getAllIseLst = createSelector(getISEManagementState, iseManage.getISELst);
export const getISEId = createSelector(getISEManagementState, iseManage.getISEID);
export const getISEInfo = createSelector(getISEManagementState, iseManage.getISEInfo);
export const getISECardInfo = createSelector(getISEManagementState, iseManage.getCardInfo);
export const getIOPsData = createSelector(getISEManagementState, iseManage.getIOPChartData);
export const getLatencyData = createSelector(getISEManagementState, iseManage.getLantencyChartData);
export const getDataRateData = createSelector(getISEManagementState, iseManage.getDataRateChartData);
export const getqDepthData = createSelector(getISEManagementState, iseManage.getqDepthChartData);
export const getIseBlinkStatus = createSelector(getISEManagementState, iseManage.getISEBlinkStatus);
export const getIseDiscovery = createSelector(getISEManagementState, iseManage.getISEDiscovery);
export const getIseDetail = createSelector(getISEManagementState, iseManage.getISEDetail);



//Menu
export const getMenuData = createSelector(getMenuState, menu.getMenuList);
export const getHostData = createSelector(getMenuState, menu.getHostList);
