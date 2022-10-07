import './App.css';
import Header from './components/Header/header';
import Body from './components/Body/body';

const bgpicture = new URL("",import.meta.url)

function App() {
  return (
    <section className='main-container'>
      
      <div className="App">
        <img src={bgpicture}/>
        <div className='App-Header'><Header /></div>
        <div><Body /></div>
      </div>
    </section>
  );
}

export default App;