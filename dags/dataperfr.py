from airflow import DAG
from airflow.operators.bash import BashOperator
import pendulum
from airflow.decorators import task
from airflow.operators.docker_operator import DockerOperator



default_args = {
    'owner': 'airflow',
    'concurrency': 1,
    'retries': 0,
    'depends_on_past': False
}

with DAG(
    dag_id='dataperf',
    schedule_interval=None,
    start_date=pendulum.datetime(2022, 7, 22, tz="UTC"),
    catchup=False
) as dag:
    t1 = BashOperator( task_id='create-baselines', bash_command='cd /opt/airflow/dags/dependency; python create_baselines.py')
    t2 = BashOperator( task_id='main', bash_command='cd /opt/airflow/dags/dependency; python main.py')
    t3 = BashOperator( task_id='plotter', bash_command='cd /opt/airflow/dags/dependency; python plotter.py')
    t4 = BashOperator( task_id='plotter-speed', bash_command='cd /opt/airflow/dags/dependency; python plotter_speed.py')

t1>>t2>>t3>>t4