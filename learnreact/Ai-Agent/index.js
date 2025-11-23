import 'dotenv/config';
import  {Agent, run} from '@openai/agents';

const helloAgent = new Agent({
    name: 'Hello Agent',
    instructions: 'You are an agent that always says hello World.',
})

run(helloAgent,'Hey There, My name is Vedant')
.then(result => {
    console.log(result.finalOutput);
});

