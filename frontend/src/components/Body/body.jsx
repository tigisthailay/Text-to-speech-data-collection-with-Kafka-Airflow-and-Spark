import React, {useState} from 'react';
//import RecorderControls from '../recorder-controls';
//import RecordingsList from "../../handlers/recordings-list";
import useRecorder from "../../hooks/useRecorder";

//import axios from 'axios';

const Body = () =>{
    const [userData, setUserData] = useState({});
    const [file, setFile] = useState();
    const [componentToShow, setComponentToShow] = useState({
        record: true,
        send: false,
    });
    const {recorderState, ...handlers} = useRecorder();
    const{ audio } = recorderState;


const handleShowSendComponent = () => {
    setComponentToShow({record: true, send: true});
};

const handleShowRecordComponent = () => {
    setComponentToShow({record: true, send: false});
};

function handleChange(event) {
    setFile(event.target.files[0]);
};

function handleClick(event) {
    event.preventDefault();
    const responses = [
        {
            id: "14e06377-62ea-4d3d-be34-76cd6aa6a737",
            headline: "ድርጅቱ ከባንኮች ጋር መሥራቱ አስተማማኝ የክፍያ ሥርዓት እንዲፈጠር አስችሏል",
            article:
              "የኢትዮጵያ የምርት ገበያ ድርጅት ከባንኮች ጋር\xa0 በጋራ በመስራቱ በተገበያዮች ላይ የክፍያ መተማመን እንዲፈጠር ማስቻሉን አስታውቋል፡፡ምርት\xa0 ገበያው ከአሁን ቀደም ከአስር ባንኮች ጋር በጋር በመስራቱ ላለፉት ዘጠኝ ዓመታት\xa0 በሚያከናውነው የግብይት ሂደት ላይ \xa0መተማመንን \xa0የፈጠረ የክፍያ ሥርዓት እንዲኖር አስችሏል ብሏል፡፡በዛሬው ዕለት ምርት ገበያው ከብርሃን ኢንተርናሽናል ባንክ ጋር በጋር\xa0 ለመስራት የሚያስችለውን ስምምነት ተፈራርሟል፡፡የአሁኑን ስምምነት ተከትሎ ምርት ገበያው ደንበኞቹ በአስራ አንድ ባንኮች የክፍያ አገልግሎት መፈጸም\xa0 እንዲችሉ የሚያደርግ ነው፡፡በአሁኑ ወቅት ድርጅቱ በዘጠኝ የሀገሪቱ አካባቢዎች እየገነባቸው ባሉ የግብይት መፈፀሚያ ማዕከላት ሻጭና አቅራቢዎች የክፍያ አገልግሎት እንዲፈጽሙ የሚያስችል ነው ብለዋል ዋና ስራ አስፈፃሚው አቶ ኤርሚያስ እሸቱ፡፡\xa0",
            audio: "../data/test_amharic.wav",
          },
          {
            id: "a658979e-8642-4fa4-9fc6-5d48286d6dc4",
            headline: "ወልዋሎ የአራት ተጫዋቾች ዝውውር አጠናቀቀ",
            article:
              "በዝውውሩ በስፋት እየተሳተፉ የሚገኙት ወልዋሎዎች ከወር በፊት ቀድመው የተስማሙት ኢታሙና ኬይሙኔ ፣ ዓይናለም ኃይሉ ፣ ኬኔዲ አሺያ እና ጆናስ ሎሎን አስፈርመዋል።የእግር ኳስ ህይቱ በተወለደበት ከተማ ዓዲግራት ጀምሮ ሃገሩን ለማገልገል ወደ መከላከያ ሰራዊት ባቀናበት ወቅት ባሳየው ጥሩ አቋም ባህር ዳር ዩኒቨርሲቲ ቀጥሎም መከላከያን የተቀላቀለው  ተከላካዩ ዓይናለም ኃይለ ከዚህ ቀደም ለደደቢት፣ ዳሽን ቢራ፣ ፋሲል ከነማ እንዲሁም ለኢትዮጵያ ብሄራዊ ቡድን መጫወቱ ይታወሳል።ሌሎች ወልዋሎ የተቀላቀሉት ናሚቢያዊያኑ ኢታሙና ኬይሙኔ እና ጆናስ ሎሎ ናቸው። ኢታሙና ባለፈው ዓመት ከብርቱካናማዎቹ ጋር የተሳካ ቆይታ የነበረው ተጫዋች ሲሆን በግብፁ የአፍሪካ ዋንጫም ተሳታፊ እንደነበር ይታወሳል። ሌላው አዲስ የቢጫ ለባሾቹ ፈራሚ ጆናስ ሎሎ ሲሆን ከኢታሙና ቀጥሎ በፕሪምየር ሊጉ የተጫወተ ሁለተኛው ናሚቢያዊ እንደሚሆን ይጠበቃል።አራተኛው የወልዋሎ ፈራሚ ከዚ በፊት በሲዳማ ቡና ቆይታ የነበረው ኬኔዲ አሺያ ነው። ተጫዋቹ በወቅቱ ከፍተኛ ክፍያ በ2009 ክረምት ክለቡን ቢቀላቀልም ብዙም ሳይቆይ መለያየቱ ይታወሳል።ቡድኑን በአዲስ መልክ እያዋቀረ የሚገኘው ወልዋሎ እስካሁን 13 ተጫዋቾች አስፈርሟል።",
            audio: "../data/test_amharic.wav",
          },
    ];
    const random = Math.floor(Math.random() * responses.length);
    console.log(random, responses[random]);
    setUserData(responses[random]);
}
//Audio Sumit button

//In the next section we will be rendering the two components of the body which are a section for getting a text and a section for reciving an audio

return (
    <>
      {/* Get text */}
      <div className="body-container">
        <section>
          <form onClick={handleClick}>
            <div className="">
              <button className=""  type="click">START</button>
            </div>
          </form>
        </section>
        <section>
          <div>
            <button className="" onClick={handleShowRecordComponent}>Insert File</button>
            <button className="" onClick={handleShowSendComponent}>RECORD</button>
          </div>
          <div>
            <p className="">{userData.headline}</p>
          </div>
        </section>
                {/* Upload audio */}
                <div>
          {componentToShow.record && (
            <div>
              <div className=''>
                <div className=''>
                  <div>
                    <form onSubmit={handleShowRecordComponent}>
                      <input type="file" onChange={handleChange} />
                      <button type="submit">Submit</button>
                    </form>
                  </div>
                  <section>
                    <p>{userData.success}</p>
                  </section>
                </div>
              </div>
            </div>
          )}{" "}
        </div>

        {componentToShow.send && (
          <div>
            <div className="" />
            <section className="">
            <h3>Readout Loud</h3>
                <div className="recorder-container">
                    
                </div>
            </section>
          </div>
        )}{" "}
      </div>
    </>
  );
};
export default Body;