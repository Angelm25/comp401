package testcompany.myapplication;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.os.Vibrator;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;


public class MainActivity extends ActionBarActivity {

    public final static String EXTRA_MESSAGE = "com.testcompany.myapplication.MESSAGE";

    public void sendMessage(View view) {
        Intent intent = new Intent(this, DisplayMessageActivity.class);
        EditText editText = (EditText) findViewById(R.id.edit_message);
        String message = editText.getText().toString();
        intent.putExtra(EXTRA_MESSAGE, message);
        startActivity(intent);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        getSupportActionBar().setDefaultDisplayHomeAsUpEnabled(true);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        MenuInflater inflater = getMenuInflater();
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return super.onCreateOptionsMenu(menu);
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        switch (item.getItemId()) {
            case R.id.action_search:
                //openSearch();
                return true;
            case R.id.action_settings:
                //openSettings();
                return true;
            default:
                return super.onOptionsItemSelected(item);
        }
    }

}
//public class MorseCode extends Activity
//{
//    /** Our text view */
//    private TextView mTextView;
//
//    /**
//     * Initialization of the Activity after it is first created.  Must at least
//     * call {@link android.app.Activity#setContentView setContentView()} to
//     * describe what is to be displayed in the screen.
//     */
//    @Override
//    protected void onCreate(Bundle savedInstanceState)
//    {
//        // Be sure to call the super class.
//        super.onCreate(savedInstanceState);
//
//        // See assets/res/any/layout/hello_world.xml for this
//        // view layout definition, which is being set here as
//        // the content of our screen.
//        setContentView(R.layout.morse_code);
//
//        // Set the OnClickListener for the button so we see when it's pressed.
//        findViewById(R.id.button).setOnClickListener(mClickListener);
//
//        // Save the text view so we don't have to look it up each time
//        mTextView = (TextView)findViewById(R.id.text);
//    }
//
//    /** Called when the button is pushed */
//    View.OnClickListener mClickListener = new View.OnClickListener() {
//        public void onClick(View v) {
//            // Get the text out of the view
//            String text = mTextView.getText().toString();
//
//            // convert it using the function defined above.  See the docs for
//            // android.os.Vibrator for more info about the format of this array
//            long[] pattern = MorseCodeConverter.pattern(text);
//
//            // Start the vibration
//            Vibrator vibrator = (Vibrator)getSystemService(Context.VIBRATOR_SERVICE);
//            vibrator.vibrate(pattern, -1);
//        }
//    };
//}
//
