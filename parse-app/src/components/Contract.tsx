import React from 'react';

const Contract = (message) => {

      console.log(message);

      const contractDict = message.message;

      console.log(JSON.stringify(contractDict));

      return (
        <div>
          <h2>Parsed Contract</h2>
          <p>Buyer: {contractDict.buyer.firstName} {contractDict.buyer.lastName}</p>
          <p>Seller: {contractDict.seller.firstName} {contractDict.seller.lastName}</p>
          <p>Date: {contractDict.dt}</p>
          <p>Deopist: {contractDict.deposit.depositAmount} in the form of a {contractDict.deposit.form}</p>
          <p>Address: {contractDict.prprty.streetNumber} {contractDict.prprty.street}, {contractDict.prprty.city}, {contractDict.prprty.state}, {contractDict.prprty.zipCode} ({contractDict.prprty.county} county)</p>

          <p>Tax ID: {contractDict.taxId}</p>          
        </div>
      );
};

export default Contract;