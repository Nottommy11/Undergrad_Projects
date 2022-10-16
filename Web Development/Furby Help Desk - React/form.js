import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

class Form extends React.Component {
    constructor(props){
        super(props)
        this.state = {
            submited: false,
            ticket: null
        };
    }

    printResults = (e)=>{
        e.preventDefault();
        this.setState({submited: true})

        // const el = React.createElement('<br/>');
        let fname = document.querySelector("#fname");
        let lname = document.querySelector("#lname");
        let furbyName = document.querySelector("#furbyName");
        let issue = document.querySelector("#issue");
        // let results = document.querySelector("#results");

        let ticket =
        {
            ticketsid: "#"+this.props.ticketId,
            firstName: fname.value,
            lastName: lname.value,
            furbyName:furbyName.value,
            furbyIssue:issue.value        
        }
        
        this.setState({ticket: ticket})
        this.props.pushTicket(ticket)
        
        /*
        let formToggle = document.querySelector("#formBox");
          formToggle.style.display= "none";
          let submittedInfoToggle = document.querySelector("#submittedInfo");
          submittedInfoToggle.style.display="block";
*/
    }

    render(){
        // const displayResults = {

        // }
        return(
            <div id="container2">
                <div id="main">

                    {
                    !this.state.submited ?
                        <form  method="get" onSubmit={this.printResults}>
                            <label for="fname">First name:</label>
                            <input type="text" id="fname" name="fname"/><br/><br/>

                            <label for="lname">Last name:</label>
                            <input type="text" id="lname" name="lname"/><br/><br/>
                            
                            <label type="furbyName">Furby's Name:</label>
                            <input type="text" id="furbyName" name="furbyName"/><br/><br/>

                            <label type="issue">Furby's Issue:</label><br/>
                            <textarea  id="issue" name="issue" rows="3" text="text" cols="60"></textarea> <br/><br/>
                            
                            <input className="block" type="submit" value="Submit" />

                        </form>
                    :
                        <div>{// style={{textAlign: "center", width: "400px"}}>
                            }
                            <h2>Ticket has been submitted!</h2>
                            <h3>Ticket Details: </h3>
                            <div style={{textAlign: "left", paddingLeft: "50px"}}>
                                {"Ticket Number: " + this.state.ticket.ticketsid}
                                <br></br>
                                {"First Name: " + this.state.ticket.firstName}
                                <br></br>
                                {"Last Name: " + this.state.ticket.lastName}
                                <br></br>
                                {"Furby's Name: " + this.state.ticket.furbyName}
                                <br></br>
                                {"Description of Issue: " + this.state.ticket.furbyIssue}
                                <br></br>
                                
                            </div>
                            <br/><br/>
                            
                            <input className="block" onClick={()=>this.setState({submited:false})} value="Submit another ticket?" />

                        </div>
                    }
                </div>
                
                <div id="sidebar">
                    <img src={require("./images/furbyOne.jpg")} alt="picture of furby"></img>
                </div>
                {/* <Form myProp={this.state.tickets} /> */}
            </div>

            
        );
        
    }

}
export default Form