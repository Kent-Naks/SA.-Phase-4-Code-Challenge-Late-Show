import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import rootReducer from './reducers';  // Import combined reducers

const store = createStore(rootReducer, applyMiddleware(thunk));

export default store;
