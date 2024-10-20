# from apscheduler.schedulers.asyncio import AsyncIOScheduler
# from apscheduler.jobstores.memory import MemoryJobStore
# from sqlalchemy.future import select

# scheduler = AsyncIOScheduler(timezone="Asia/Yekaterinburg")
# jobstore = MemoryJobStore()


# scheduler.add_jobstore(jobstore=jobstore)
# from ..core.database import sessionmaker
# from ..models.models import WellsModel


# async def init_pairs():
#     scheduler.remove_all_jobs(jobstore)
#     async with sessionmaker() as session:

#         result = await session.execute(select(WellsModel))  # type: ignore
#         wells = result.scalars().all()
#         for well in wells:
#             scheduler.add_job(
#                 pair_starter,
#                 "cron",
#                 hour=slot.start_time.hour,
#                 minute=slot.start_time.minute,
#                 second=slot.start_time.second,
#                 args=[slot.id],
#             )  # type: ignore
#             logger.info(
#                 f"Pair starter job scheduled to: {slot.start_time.hour}:{slot.start_time.minute}"
#             )
#             scheduler.add_job(
#                 pair_ender,
#                 "cron",
#                 hour=slot.end_time.hour,
#                 minute=slot.end_time.minute,
#                 second=slot.end_time.second,
#                 args=[slot.id],
#             )  # type: ignore
#             logger.info(
#                 f"Pair ender job scheduled to: {slot.end_time.hour}:{slot.end_time.minute}"
#             )


# async def send_message():
#     scheduler.remove_all_jobs(jobstore)
#     async with sessionmaker() as session:

#         result = await session.execute(select(WellsModel))  # type: ignore
#         wells = result.scalars().all()
#         result = await session.execute(select(WellsModel))  # type: ignore
#         wells = result.scalars().all()
#         for well in wells:
#             scheduler.add_job(
#                 pair_starter,
#                 "cron",
#                 hour=slot.start_time.hour,
#                 minute=slot.start_time.minute,
#                 second=slot.start_time.second,
#                 args=[slot.id],
#             )  # type: ignore
#             logger.info(
#                 f"Pair starter job scheduled to: {slot.start_time.hour}:{slot.start_time.minute}"
#             )
#             scheduler.add_job(
#                 pair_ender,
#                 "cron",
#                 hour=slot.end_time.hour,
#                 minute=slot.end_time.minute,
#                 second=slot.end_time.second,
#                 args=[slot.id],
#             )  # type: ignore
#             logger.info(
#                 f"Pair ender job scheduled to: {slot.end_time.hour}:{slot.end_time.minute}"
#             )


# @scheduler.scheduled_job("interval", seconds=10)
# def synchronizer():
#     print("scheduled_job_1")


# # Job running at a specific date and time
# @scheduler.scheduled_job("date", run_date="2024-07-21 11:00:00")
# def scheduled_job_2():
#     print("scheduled_job_2")


# # Job running daily at 23:44:00
# @scheduler.scheduled_job("cron", day_of_week="mon-sun", hour=23, minute=44, second=0)
# def scheduled_job_3():
#     print("scheduled_job_3")
