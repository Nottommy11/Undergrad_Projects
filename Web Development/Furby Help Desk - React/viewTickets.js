import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

class ViewTicket extends React.Component {
    constructor(props){
        super(props)
        this.state = {
        };
    }

    render(){
        console.log(this.props.allTickets);
        let allTickets = this.props.allTickets;
    const displayAllTickets = allTickets.map(tickets => {
        
        return(
    
            <li>
                 <h3>Ticket Id: {tickets.ticketsid}</h3> 
                 <ul>
                 <li> First Name: {tickets.firstName} </li>
                 <li> Last Name: {tickets.lastName} </li>
                 <li> Furby's Name: {tickets.furbyName} </li>
                 <li> Descritption of Issue: {tickets.furbyIssue} </li>
                 <li> Status: Active </li>
                 </ul>
            </li>
           
        ) 
    })
        return(
            <div id="container2">
                <div id="main">
                    <ol>
                     {displayAllTickets}
                    </ol>
                </div>
                <div id="sidebar">
                <img src={require("./images/Optimistic_Furby2.png")} alt="picture of furby"></img>
                </div>
            </div>
        );
    }
}
export default ViewTicket