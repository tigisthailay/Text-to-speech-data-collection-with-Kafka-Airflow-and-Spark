import './App.css';
import Header from './components/Header/header';
import Body from './components/Body/body';

function App() {
  return (
    <div>
      <div className="App">
        <div className='App-Header'><Header /></div>
        <div><Body /></div>
      </div>
    </div>
  );
}

export default App;
