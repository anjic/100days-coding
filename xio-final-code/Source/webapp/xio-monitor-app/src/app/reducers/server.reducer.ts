
import * as server from '../actions/server.actions';

export interface State {
  serverLst: Array<Object>;
  ServerDetails: Object;
  Server:any
  wwn:any;
  wwnGroups:any;
  serverWwnGroups:any;
  serversideise:any;

};

export const initialState: State = {
  serverLst: [],
  ServerDetails: {},
  Server:{},
  wwn:{},
  wwnGroups:{},
  serverWwnGroups:{},
  serversideise:{}
 };

export function reducer(state = initialState, action: server.Actions): State {
  switch (action.type) {

    case server.GET_ALL_SUCCESS: {
      return {
        serverLst: action.payload,
        ServerDetails: state.ServerDetails,
        Server:state.Server,
        wwn:state.wwn,
        wwnGroups:state.wwnGroups,
        serverWwnGroups:state.serverWwnGroups,
        serversideise:state.serversideise

      }
    }

    case server.GET_WWN_SUCCESS: {
      return {
        serverLst: state.serverLst,
        ServerDetails: state.ServerDetails,
        Server:state.Server,
        wwn:action.payload,
        wwnGroups:state.wwnGroups,
        serverWwnGroups:state.serverWwnGroups,
        serversideise:state.serversideise

      }
    }

    case server.GET_ALL_WWN_GROUPS_SUCCESS: {
      return {
        serverLst: state.serverLst,
        ServerDetails: state.ServerDetails,
        Server: state.Server,
        wwn: state.wwn,
        wwnGroups: action.payload,
        serverWwnGroups:state.serverWwnGroups,
        serversideise:state.serversideise

      }
    }

    case server.GET_SERVERSIDE_WWN_GROUPS_SUCCESS: {
      return {
        serverLst: state.serverLst,
        ServerDetails: state.ServerDetails,
        Server: state.Server,
        wwn: state.wwn,
        wwnGroups: state.wwnGroups,
        serverWwnGroups:state.serverWwnGroups,
        serversideise:action.payload

      }
    }

    case server.ADD_SERVER_SUCCESS: {
      return {
        Server:action.payload,
        serverLst:state.serverLst,
        ServerDetails:state.ServerDetails,
        wwn:state.wwn,
        wwnGroups:state.wwnGroups,
        serverWwnGroups:state.serverWwnGroups,
        serversideise:state.serversideise


      }
    }

    // case server.UPDATE_SERVER_SUCCESS: {
    //   return {
    //     serverLst: [...state.serverLst.map((sg) => {
    //       if (ser['server_id'] === action.payload[0].server_id) {
    //         return action.payload[0];
    //       }
    //       else {
    //         return sg;
    //       }
    //     })],
    //     ServerDetails: state.ServerDetails,

    //   }
    // }
    case server.DELETE_SERVER_SUCCESS: {
      return {
        serverLst: action.payload,
        ServerDetails: state.ServerDetails,
        Server:state.Server,
        wwn:state.wwn,
        wwnGroups:state.wwnGroups,
        serverWwnGroups:state.serverWwnGroups,
        serversideise:state.serversideise

      }
    }

    case server.GET_SERVER_SUCCESS: {
      return {
        serverLst: state.serverLst,
        ServerDetails: state.ServerDetails,
        Server:action.payload,
        wwn:state.wwn,
        wwnGroups:state.wwnGroups,
        serverWwnGroups:state.serverWwnGroups,
        serversideise:state.serversideise

      }
   }
    case server.GET_SERVER_WWNGROUPS_SUCCESS: {
      return {
        serverLst: state.serverLst,
        ServerDetails: state.ServerDetails,
        Server:state.Server,
        wwn:state.wwn,
        wwnGroups:state.wwnGroups,
        serverWwnGroups:action.payload,
        serversideise:state.serversideise

      }
    }

    case server.UPDATE_WWN_GROUP_SUCCESS: {
      return {
        serverLst: state.serverLst,
        ServerDetails: state.ServerDetails,
        Server:state.Server,
        wwn:state.wwn,
        wwnGroups:state.wwnGroups,
        serverWwnGroups:state.serverWwnGroups,
        serversideise:state.serversideise

      }
    }

        default: {
      return state;
    }
  }
}

export const getServerLst = (state: State) => state.serverLst || [];
export const getServer = (state : State) => state.Server;
export const getWwn =  (state: State) => state.wwn || [];
export const getAllWwnGroups = (state: State) => state.wwnGroups || [];
export const getAllServerWwnGroups = (state: State) => state.serverWwnGroups || [];
export const getServerSideWwnGroups = (state: State) => state.serversideise || [];
