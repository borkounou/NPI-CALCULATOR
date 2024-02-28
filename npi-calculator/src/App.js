import './App.css';
import React, {useState} from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css'


function App() {
  const [expression, setExpression] = useState('');
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null); // State to hold error message
  const [csvMessage, setCsvMessage] = useState(null)

  const submitHandler = ()=>{
      axios.post('http://127.0.0.1:8000/api/calculator',{'expression':expression}).then(res=>{
        setResult(res.data.result); 
        setError(null);
      
    }).catch(error=>{
      // console.error('Error:', error);
      setResult(null); // Reset result state
      setError('Something went wrong. Please type a valid expression.');

    });
  };


  const handleExportToCSV = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/calculator', {
        responseType: 'blob' // Set response type to blob to receive binary data
      });
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', 'expressions_results.csv');
      document.body.appendChild(link);
      link.click();
      setCsvMessage('Your result is saved in the CSV file.');
    } catch (error) {
      console.error('Error:', error);
      setCsvMessage('Error occurred while saving to CSV.');
    }
  };


  return (
      <div className='App list-group-item justify-content-center align-items-center mx-auto' style={{"width":"400px", "backgroundColor":"white", "marginTop":"15px"}}>
          <h1 className='card text-white bg-primary mb-1' styleName="max-width:20rem;"> NPI Calcultor</h1>

          <h6 className='card text-white bg-primary mb-3'> Polish Reverse Notation Calculator</h6>
          <div className='card-body'>
          <h5 className='card text-white bg-dark mb-3'>Type your expression</h5>
          <span className='card-text'>
          <input className='mb-2 form-control titleIn' onChange={event=>setExpression(event.target.value)} placeholder='2 2 + 3 /' />
          <button className='btn btn-outline-primary mx-2 mb-3' style={{'borderRadius':'50px', 'font-weight':'bold' }} onClick={submitHandler}>Calculate</button>
          </span>

          {error && (
          <div className="alert alert-danger" role="alert">
            {error}
          </div>
        )}

          {result !== null && (
          <>
            <h5 className='card text-white bg-dark mb-3'>Result:</h5>
            <div className='mb-3'>
              <strong>{result}</strong>
            </div>
            <button className='btn btn-outline-primary mx-2 mb-3' style={{ 'borderRadius': '50px', 'fontWeight': 'bold' }} onClick={handleExportToCSV}>Export to CSV</button>
          </>
        )}


        {csvMessage && (
          <div className="alert alert-success" role="alert">
            {csvMessage}
          </div>
        )}


          </div>


          <h6 className='card text-dark bg-warning py-1 mb-0'>Copyright 2024, All rights reserved &copy;</h6>
      </div>


  );
}

export default App;
