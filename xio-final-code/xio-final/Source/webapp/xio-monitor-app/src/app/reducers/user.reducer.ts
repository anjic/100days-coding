
import * as user from '../actions/user.actions';
import { User } from '../user/models/user';

export interface State{
  user_list:Array<User>,
  user:Object,
  auth: Object
};

export const initialState: State = {
  user_list: [{
    'id': 0,
    'first_name': '',
    'last_name': '', 
    'username': '',
    'email': '',
    'password': '',
  }],
    user:{},
    auth: {
      username: 'Administrator',
  }
};

export function reducer(state = initialState, action:  user.Actions) : State {
  switch(action.type){
    case user.GET_ALL_USERS_SUCCESS:{
      return {
        user_list: action.payload,
        user:state.user,
        auth: state.auth
      }
    }


    case user.GET_USER_SUCCESS:{
      return{
        user:action.payload,
        user_list:state.user_list,
        auth: state.auth
      }
    }

    case user.SAVE_USER_SUCCESS:{
      return{
        user:state.user,
        user_list:state.user_list,
        auth: state.auth
      }
    }

    case user.UPDATE_USER_SUCCESS:{
      return{
        user:state.user,
        user_list:state.user_list,
        auth: state.auth
      }
    }

    case user.DELETE_USER_SUCCESS:{
      return{
        user:state.user,
        user_list:state.user_list,
        auth: state.auth
      }
    }

    default: {
      return state;
    }
  }
}

export const getUserLst = (state : State) => state.user_list;
export const getUser = (state : State) => state.user;
export const getAuthInfo = (state : State) => state.auth;
