import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

class HelpSheet extends React.Component {
    constructor(props){
        super(props)
        this.state = {
        };
    }

    

    render(){
        return(
            <div id="container2">
                <div id="main">
                    <h2>Common FAQS for Furby</h2>
                    <p>If your Furby won't turn on try:</p>
                    <ul>
                        <li>Fully reset your Furby. <br/>
                            If this does not help try resetting your Furby
                            while it is upside down, and hold its tongue.
                        </li>
                    </ul>

                    <p>I dropped my Furby and now it is screaming!</p>
                    <ul>
                        <li>Fully reset your Furby. <br/>
                            This should stop the screaming.
                        </li>
                    </ul>

                    <p>My Furby keeps shaking!</p>
                    <ul>
                        <li>Fully press down on your Furby's tongue, give your Furby a shake, 
                            let go of its tongue, and turn it right away.
                        </li>
                    </ul>

                    <p>How do I get my Furby to be normal again?</p>
                    <ul>
                        <li>There is no such thing as a "normal" Furby.
                        </li>
                    </ul>
                </div>
                <div id="sidebar">
                    <h2>Emergency?</h2>
                    <p>Furby gone goblin and has robot rabies? Call:</p>
                    <ul>
                        <li>(402) 372-2116 </li>
                    </ul>
                    <p>Furby being controlled by a ghost? Who you gonna call:</p>
                    <ul>
                        <li>(402) 372-2116 </li>
                    </ul>
                    <p>Has your Furby taken the local orphanage hostage again? Call:</p>
                    <ul>
                        <li>911</li>
                        <li>Mention Code Silver</li>
                    </ul>
                </div>
            </div>
        );
    }
}
export default HelpSheet