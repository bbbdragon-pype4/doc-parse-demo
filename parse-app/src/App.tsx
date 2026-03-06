import './App.css';

import SingleImageFileUploader from './components/SingleImageFileUploader';

function App() {
  return (
    <>
      <h1>Real Estate Contract JPEG Parser</h1>

      <SingleImageFileUploader/>

      <p className="read-the-docs">This app is built with Vite and React.</p>
    </>
  );
}

export default App;