from aiogram.types import ReplyKeyboardMarkup, KeyboardButton , InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

youtubers = ["Marmok", "Utopia show", "Weezzy"]

pod_obz = ["дальше" , "назад"]



dalshe_nazad = InlineKeyboardMarkup(inline_keyboard=[
     [InlineKeyboardButton(text="дальше" , callback_data="dal" )],
     [InlineKeyboardButton(text="назад" , callback_data="baz" )],
])

wubor_kategori = InlineKeyboardMarkup(inline_keyboard=[
     [InlineKeyboardButton(text="3 вашы подписки " , callback_data="3" )],
     [InlineKeyboardButton(text="4 все " , callback_data="4" )],

 ])


def obzor_kanal(channel_id):
    kb = InlineKeyboardBuilder()

    kb.button(
        text="Обзор",
        callback_data=f"view_{channel_id}"
    )
    kb.button(
        text="Подписаться",
        callback_data=f"sub_{channel_id}"
    )

    kb.adjust(2)
    return kb.as_markup()


oplata_podpiski = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="оплатить подписку" , callback_data="1" )],
    [InlineKeyboardButton(text="продолжыть подписку" , callback_data="2" )]
 ])



def kanal_buttons(channel_id: int):
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Обзор", callback_data=f"view_{channel_id}"),
            InlineKeyboardButton(text="Подписаться", callback_data=f"sub_{channel_id}")
        ]
    ])

pagination = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад", callback_data="page_back"),
        InlineKeyboardButton(text="Дальше", callback_data="page_next"),
    ]
])

