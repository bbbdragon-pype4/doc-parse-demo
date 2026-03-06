import React, { useState } from 'react';
import Contract from './Contract';
import ModelSelector from './ModelSelector';
import styles from './SingleImageFileUploader.module.css';

const MODEL_TO_API = {'OCR':'/api/ocr',
                      'LLM Image Buffer':'/api/llm_image',
                      'Hybrid':'/api/hybrid',
                     };

const model_api_from_str = (st: string) => {

  if (!(st in MODEL_TO_API)) {
     
     console.log('Did not find this option in MODEL_TO_API');
     console.log(st);
     
     return MODEL_TO_API['OCR'];
  }

  return MODEL_TO_API[st];
};

const SingleImageFileUploader = () => {
  const [imageSrc, setImageSrc] = useState<string | null>(null);
  const [contractDict, setContractDict] = useState<Object | null>('');
  const [selectedModel, setSelectedModel] = useState("OCR");
  const modelOptions = ["OCR", "LLM Image Buffer", "Hybrid"];

  const handleFileChange = async (e: React.ChangeEvent<HTMLInputElement>) => {

    const file = e.target.files?.[0];

    if (file && file.type.substring(0,5) == 'image') {

      console.log('Uploading file...');
      console.log(file);

      const objectURL = URL.createObjectURL(file);
            
      setImageSrc(objectURL);
             
      const formData = new FormData();

      formData.append('file',file);

      try {
        
        const api = model_api_from_str(selectedModel);
        // You can write the URL of your server or any other endpoint used for file upload
        const result = await fetch(api, {
          method: 'POST',
          body: formData,
        });

        const data = await result.json();
        const contractDict = data.message;

        setContractDict(contractDict);

        console.log('getting back data');
        console.log(contractDict);
      } catch (error) {
        console.error(error);
      }
      
    } else {
      setImageSrc(null);
      setParsedImage(null);
    }
  };

  return (
    <div>
      <h2>Upload and Display a JPEG Image of a Contract</h2>
      <input
        type="file"
        accept="image/jpeg" // Restrict to JPEG files
        onChange={handleFileChange}
      />

      <div>
        <h2>Select Your Model</h2>
        {/* Pass state and the setter function down as props */}
        <ModelSelector 
          options={modelOptions} 
          selectedValue={selectedModel} 
          onSelectionChange={setSelectedModel} 
        />
      </div>

      {/* Display the image preview if imageSrc is available */}
      {imageSrc && (
        <div className={styles.imagePreviewMargin}>
          <h2>Image Preview:</h2>
          <img
            src={imageSrc}
            alt="Uploaded preview"
            className={styles.imageSize}
           />
        </div>
      )}

      {(imageSrc && !contractDict) && ( 
        <div className={styles.imagePreviewMargin}>
          <p>Processing file ...</p>
        </div>
      )}

      {contractDict && ( 
        <div className={styles.imagePreviewMargin}>
          <Contract message={contractDict}/>
        </div>
      )}
    </div>  
  );
};

export default SingleImageFileUploader;