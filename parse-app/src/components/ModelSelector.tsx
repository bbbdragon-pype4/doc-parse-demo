import React from 'react';

const ModelSelector = ({options, selectedValue, onSelectionChange}) => {

  return (
    <div>
      {options.map((option) => (
        <label key={option}>
          <input
            type="radio"
            name="dynamic-group"
            value={option}
            checked={selectedValue === option} // Controlled by parent prop
            onChange={(e) => onSelectionChange(e.target.value)} // Sends value back UP
          />
          {option}
        </label>
      ))}
    </div>
  );
};

export default ModelSelector;